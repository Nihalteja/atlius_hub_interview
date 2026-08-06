def dedupe_latest(events):
    latest = {}

    for ev in events:
        eid = ev["event_id"]
        if eid not in latest or ev["ts"] > latest[eid]["ts"]:
            latest[eid] = ev
    return sorted(latest.values(), key=lambda e: e['ts'])


def apply_events(events, ledger):
    ledger = ledger.copy()
    for ev in dedupe_latest(events):
        inv = ev["payload"]["invoice_id"]
        if ev["type"] == "paid":
            ledger[inv] = "paid"
        elif ev["type"] == "void":
            ledger[inv] = "void"
        
    return ledger