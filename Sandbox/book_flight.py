def book_flight(fromairport, toairport, numadults=1, numchildren=0):
    if fromairport is None:
        fromairport = "JFK"
    if toairport is None:
        toairport = "JFK"
    print("\nFlight booked from %s to %s" % (fromairport, toairport))
    print("Number of adults: %d" % numadults)
    print("Number of children: %d" % numchildren)


book_flight('AMS', 'LHR', 2, 3)
book_flight('AMS', 'LHR', 2)
book_flight('AMS', 'LHR')

book_flight('AMS', 'LHR', numchildren = 3)

book_flight(toairport='AMS', numchildren = 3)

