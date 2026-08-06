def fetch_all_invoices(client, org_id, page_size=50):
    import math
    first = client.list_invoices(org_id, page=0, page_size=page_size)
    total = first.get("total") or 0
    items = list(first.get("items") or [])
    pages = math.ceil(total/page_size)
    for page in range(1, pages):
        resp = client.list_invoices(org_id, page=page, page_size=page_size)
        items.extend(resp["items"])
    return items