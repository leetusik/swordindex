#!/usr/bin/env python
"""
Script to help submit the sitemap to Google Search Console.
This script provides instructions and a curl command to submit the sitemap.
"""

import os
import sys
import webbrowser


def submit_sitemap():
    """Provide instructions for submitting the sitemap to Google Search Console"""
    print("=" * 80)
    print("Google Search Console Sitemap Submission Helper")
    print("=" * 80)
    print(
        "\n1. Make sure you have verified ownership of your domain in Google Search Console."
    )
    print("   If not, visit: https://search.google.com/search-console/welcome")
    print("\n2. Once verified, you can submit your sitemap using one of these methods:")

    print("\n   Method 1: Submit via Google Search Console UI")
    print(
        "   - Log in to Google Search Console: https://search.google.com/search-console"
    )
    print("   - Select your property")
    print("   - In the left sidebar, click on 'Sitemaps'")
    print("   - Enter 'sitemap.xml' in the 'Add a new sitemap' field")
    print("   - Click 'Submit'")

    print("\n   Method 2: Submit via direct URL")
    print("   - Use this URL to submit (replace with your actual domain):")
    print("     https://www.google.com/ping?sitemap=https://swordindex.com/sitemap.xml")

    # Ask if user wants to open Google Search Console
    open_console = input("\nWould you like to open Google Search Console now? (y/n): ")
    if open_console.lower() == "y":
        webbrowser.open("https://search.google.com/search-console")

    # Ask if user wants to ping Google directly
    ping_google = input(
        "\nWould you like to ping Google directly with your sitemap? (y/n): "
    )
    if ping_google.lower() == "y":
        domain = input("Enter your domain (e.g., swordindex.com): ")
        if domain:
            ping_url = (
                f"https://www.google.com/ping?sitemap=https://{domain}/sitemap.xml"
            )
            print(f"\nExecuting: curl '{ping_url}'")
            os.system(f"curl '{ping_url}'")
            print("\nPing sent to Google. Note that this doesn't guarantee indexing.")

    print("\n" + "=" * 80)
    print("Additional SEO Tips:")
    print("=" * 80)
    print(
        "1. Register your site with Naver Search Advisor for better visibility in Korea:"
    )
    print("   https://searchadvisor.naver.com/")
    print(
        "\n2. Set up Google Analytics 4 to track user behavior and improve your site."
    )
    print("\n3. Regularly update your content to keep search engines coming back.")
    print("\n4. Create high-quality backlinks from relevant Korean websites.")
    print(
        "\n5. Optimize for Korean mobile search - most Korean users search on mobile."
    )
    print("=" * 80)


if __name__ == "__main__":
    submit_sitemap()
