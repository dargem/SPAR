"""
Brickfields

Main takeaways of this explanation are
    - Bricks must be a partition of the created rectangle (non overlapping with 0 gaps)

Could create a hashmap of each coord to filled/unfilled, 
when adding bricks its bounded coords must not have been already filled.
After having added bricks you would check the coordinates of the rectangle it makes are filled.
Too slow in practice with 10^8 size for x and y would require a hashmap of 10^16 size which isn't possible

This shows you need some way to track whether rectangles overlap / fill the rectangle,
without relying on the raw coords the rectangle fills or anything that involves iteration over all coordinates

If the bricks are a partition of the rectangle, 
the sum of the areas of every brick will equal the area of the rectangle.
This can be used to find if bricks perfectly cover the rectangle if it meets the assumption bricks are non overlapping

So all we need to do is find a way to check that bricks do not overlap, 
then we can take the highest x and highest y coordinate, multiply that to get area of wanted rectangle.
Then sum together areas of each brick and we have found that the bricks are a partition of the rectangle.

Looking at the images we can think of a brick as openings and closings
The opening is the left of a brick, closing is its right side.
If an opening is followed by another opening thats bad means bricks are overlapped.
Keeping in mind its not like opening at x = 1, opening at x = 2 and closing at x = 2.
That would be fine, if an opening and closing are at the same x, closing should go before it

So we would want something like a working set which is the current openings/closings for a given y
Thinking about it the working set will only change when another rectangle enters/leaves.
If the working set doesn't change we don't need another check so really it comes down to events.
A rectangle start event would occur at its starting y value, and it would add an opening and closing bracket at its x's
A rectangle close event would occur at its ending y value, and it would remove an opening and closing bracket at its x's

So at the start we need to convert our rectangles into these events basically
Where keyed by y value its associated with creating/destroying brackets
Then sort these by y value, then can discard they value or ignore it whats important is events are ordered

At our very start the working set is empty obv, we start with the very first event adding rectangles to the working set
When that event has been processed we check if the working set is valid.
We could have the working set be a binary search tree and check if it properly alternates between open/closing brackets
We can technically skip checking an end bracket should be paired on the same x value with a start bracket,
unless its the final end bracket at the very right ofc. This means bricks would be non overlapping but can have gaps.
But the bricks being non overlapping but with gaps would fail the prior mentioned area check so this would still be fine!

Doing a full check of the working set after an event is pricy though, checking the whole working set each event.
In a worst case where the working set is very large which is possible this would be n^2.
So we want to validate during the insertion/deletion event rather than after it. 
Thinking about it a deletion event could lead to an empty gap but it would never result in stuff overlapping.
Only addition would do that and we don't care about gaps since the area check at the end will catch them.
So we only need to validate when inserting a start/end edge during an event.
And order we add/remove during this event starts to matter also, so we should do all removals first.
Else there's an edge case an insertion will fail because it overlaps with a brick where the removal is just later in the same event.
And for an insertion we need to make sure these are paired, ie add an open bracket for a given brick then the close bracket together.
Else we could add the open bracket for ex, and there's no close for it since we're adding that next.
So an insertion would check there's no edges between the open/close edge.
Then that the open edge is after a close edge, and the close edge is before an open edge.
Or its after/before nothing as its at the very end.
Maybe better to think about it as an open edge is not after an open and vice versa.

Thinking about it as long as the opening edge is not after an opening edge,
and the opening / closing edge has no edges between them,
we have no need to check what happens after the closing edge as we know we haven't intersected any edges already


So in summary we need to 
- Turn rectangles into events, where an event is a list of paired insertions and a list of removals
- Order these events by y value, putting removals before insertions
- Create the empty working set
- Start progression through these events, in this event which is a list of removals and a list of insertions
    - Remove from working set in the event
    - Then add a pair into the working set, validating
        - The opening edge is not immediately after an opening edge
        - There are no edges between the opening and closing edge
- If a validation is failed, early return that there is an intersection and its therefore not a partition
- If we haven't early returned there are no intersections, now we need to find the area of the rectangle
- We know its centered at the origin.
- We now need to go find the biggest/smallest x and the biggest/smallest y value of any rectangle.
- Then find that area of that rectangle all bricks are expected to be bound in
- Then sum up the areas of every rectangle
- If these equal we now know its a partition as its non overlapping and areas perfectly sum up!
- If its not equal its non overlapping but there's gaps so its a fail
"""

num_bricks = int(input())

from enum import Enum

class Brace(Enum):
    OPENING = 0
    CLOSING = 1

class EventList:
    def __init__(self):
        self.events = {}

class Modifications:
    def __init__(self):
        self.insertions = []
        self.removals = []

event_holder = EventList()
for _ in range(num_bricks):
    start_x, start_y, width, height = map(int, input().split())

    if start_y not in event_holder.events:
        event_holder.events[start_y] = Modifications()
    if start_y + height not in event_holder.events:
        event_holder.events[start_y + height] = Modifications()
    
    event_holder.events[start_y].insertions.append((start_x, Brace.OPENING))
    event_holder.events[start_y].insertions.append((start_x + width, Brace.CLOSING))
    
    event_holder.events[start_y + height].removals.append((start_x, Brace.OPENING))
    event_holder.events[start_y + height].removals.append((start_x + width, Brace.CLOSING))

# average readable python one liners                                     
sorted_modifications = [item[1] for item in sorted(event_holder.events.items(), key=lambda y: y[0])]

class WorkingSet:
    

for mod in sorted_modifications:
