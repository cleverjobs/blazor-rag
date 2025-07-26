# How do I create dynamic Nested StackLayouts

## Question

**Joh** asked on 09 Aug 2021

I have a need for a two dimensional "grid" of cards that is dynamic in both directions. Each column is independent of the others. Something like this: Each Status/Step to the approval process could have duplicates of the Request, i.e. Request 1 is still in pending status. Request 2 has been submitted and needs Approval 1 and Approval 2. Request 3 has been submitted and needs Approval 3. I will build an ordered list with necessary duplicates to fill this. I was trying to use nested StackLayouts to do this but it does not appear to like anything dynamic. Display should be approximately like: Status Pending Submitted Approval 1 Approval 2 Approval 3 Request 1 Request 2 Request 2 Request 2 Request 3 Request 3

### Response

**John** commented on 09 Aug 2021

Here's a pared down version: <TelerikStackLayout Orientation="StackLayoutOrientation.Horizontal"> @foreach (var step in workflowsteps)
{ <div> <span> step </span> <br /> <TelerikStackLayout Orientation="StackLayoutOrientation.Vertical"> @foreach (var card in cards)
{
@if (card.step==step) <TelerikCard /> } </div> }
