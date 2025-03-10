#!/usr/bin/env python
"""
Script to generate a sitemap.xml file for the Swordindex website.
This can be run periodically to update the sitemap with new pages.
"""

import datetime
import os
from xml.dom import minidom

# Configuration
SITE_URL = "https://swordindex.com"
OUTPUT_FILE = "static/sitemap.xml"

# Define your site's pages
pages = [
    {"loc": "/", "priority": "1.0", "changefreq": "weekly"},
    {"loc": "/privacy-policy/", "priority": "0.5", "changefreq": "monthly"},
    {"loc": "/sitemap/", "priority": "0.5", "changefreq": "monthly"},
    # Add more pages as your site grows
]


def generate_sitemap():
    """Generate a sitemap.xml file"""
    # Create the XML document
    doc = minidom.getDOMImplementation().createDocument(None, "urlset", None)
    root = doc.documentElement
    root.setAttribute("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")
    root.setAttribute("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
    root.setAttribute(
        "xsi:schemaLocation",
        "http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd",
    )

    # Current date in W3C format
    today = datetime.datetime.now().strftime("%Y-%m-%d")

    # Add each page to the sitemap
    for page in pages:
        url_element = doc.createElement("url")

        # Add location
        loc = doc.createElement("loc")
        loc_text = doc.createTextNode(f"{SITE_URL}{page['loc']}")
        loc.appendChild(loc_text)
        url_element.appendChild(loc)

        # Add last modified date
        lastmod = doc.createElement("lastmod")
        lastmod_text = doc.createTextNode(today)
        lastmod.appendChild(lastmod_text)
        url_element.appendChild(lastmod)

        # Add change frequency
        changefreq = doc.createElement("changefreq")
        changefreq_text = doc.createTextNode(page["changefreq"])
        changefreq.appendChild(changefreq_text)
        url_element.appendChild(changefreq)

        # Add priority
        priority = doc.createElement("priority")
        priority_text = doc.createTextNode(page["priority"])
        priority.appendChild(priority_text)
        url_element.appendChild(priority)

        # Add the URL element to the root
        root.appendChild(url_element)

    # Write the XML to file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(doc.toprettyxml(indent="  "))

    print(f"Sitemap generated at {OUTPUT_FILE}")


if __name__ == "__main__":
    generate_sitemap()
