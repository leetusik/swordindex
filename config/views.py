import json
import os

from django.conf import settings
from django.http import FileResponse, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def index(request):
    return render(request, "index.html")


def privacy_policy(request):
    """Render the privacy policy modal content"""
    return render(request, "modal.html")


def test_static(request):
    """Test page for static files"""
    return render(request, "test_static.html")


def direct_image(request):
    """Directly serve an image file"""
    image_path = os.path.join(settings.BASE_DIR, "static", "img", "logo.png")
    if os.path.exists(image_path):
        return FileResponse(open(image_path, "rb"), content_type="image/png")
    else:
        return HttpResponse(f"Image not found at {image_path}", status=404)


def load_vector_store():
    """Load the saved vector store"""
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-large",
    )
    vector_store = FAISS.load_local(
        "data/vector_store",
        embeddings,
        allow_dangerous_deserialization=True,
    )
    return vector_store


@require_GET
def search_api(request):
    """GET API endpoint for searching packages"""
    query = request.GET.get("q", "")

    if not query:
        return JsonResponse({"error": "Query parameter 'q' is required"}, status=400)

    vector_store = load_vector_store()

    # The query is already enhanced with "kimchi" from the API
    enhanced_query = f"Find travel packages related to: {query}"

    # Search similar packages with MMR
    similar_docs = vector_store.max_marginal_relevance_search(
        enhanced_query,
        k=5,
        fetch_k=50,
        lambda_mult=1.0,
    )
    # Get the document metadata for each result
    results = [doc.metadata for doc in similar_docs]

    return JsonResponse({"results": results, "query": query})


def test(request):
    """Test page for testing"""
    return render(request, "test.html")
