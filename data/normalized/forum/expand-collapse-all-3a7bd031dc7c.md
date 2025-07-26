# Expand/Collapse All

## Question

**Cip** asked on 08 Dec 2020

Hi everyone, I wanted to implement a functionality of Expand/Collapse All. I had the property Expanded in the model which takes the value of true or false. I am changing the value of that property in the model but nothing happens on the interface. Can you help me please? Can this functionality be implemented? Thank you, Cipri

## Answer

**Ciprian Daniel** answered on 08 Dec 2020

Nevermind I've tried to implement the functionality of Expand/Collapse All using the TreeList State and I succeeded. So no worries about this thread. Best regards, Cipri

### Response

**Jonathan** answered on 13 Aug 2024

If you are looking for the answer I provided one. public class MyTreeObject { public int Id { get; set; } public Something Stuff { get; set; } public IEnumerable<MyTreeObject> Children { get; set; }
} private void ExpandAll () {
GridRef.State.ExpandedItems=new List<MyTreeObject>(); var flatList=GridData?.Flatten(x=> x.Children) ?? new List<MyTreeObject>(); foreach ( var child in flatList)
{ if (child.Children.Count> 0 )
{
GridRef.State.ExpandedItems.Add(child);
}
}
GridRef.Rebind();
StateHasChanged();
} And I borrow a Flatten method from StackOverflow here

### Response

**Hristian Stefanov** commented on 13 Aug 2024

Hello, Thank you for sharing the approach here, publicly, so other developers dealing with the TreeList expansion can benefit from it. Kind Regards, Hristian
