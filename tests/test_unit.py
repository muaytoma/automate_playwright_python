
def checkTrackingResult(r):
  if r["sta"]["code"] != "01":
    print ("\tExpected code 01 returned, but got " + r["sta"]["code"])
    return False
  if not r["shipment"]:
    print ("\tExpected to shipment element returned")
    return False
  if not r["shipment_status"]:
    print ("\tExpected to shipment_status element returned")
    return False
  return True
