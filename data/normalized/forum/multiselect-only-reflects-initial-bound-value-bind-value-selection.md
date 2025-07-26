# MultiSelect only reflects initial bound value (@bind-Value) selection

## Question

**Cha** asked on 21 Feb 2022

Hello, I'm programmatically setting the selected list (/from/ the available selection) on a MultiSelect. It's bound to a List<string> that is part of a class: data.Value. The MultiSelect is part of a "child" component that I use on more than one page. On initial load, the List<string> that it is bound to is freshly instantiated in the class: public List<string> Value {get; set; }=new(); The very first time the code populates the list, the UI properly reflects the associated names (using key/value pairs from a dictionary). After that, the UI doesn't change with further updates to the list. My original code had Value.Clear() and then Value.Add(<new string values>) as required. On a hunch, I changed it to re-instantiate the List instead of Value.Clear(), and now the UI refreshes as I expect it to. I see the example [https://docs.telerik.com/blazor-ui/components/multiselect/refresh-data](https://docs.telerik.com/blazor-ui/components/multiselect/refresh-data) first List.Clear()'s the List, then re-instantiates it, which I find odd. Why .Clear() if you're going to re-instantiate it? void ClearSelected()
{
TheValues.Clear();
TheValues=new List <int> (TheValues);
} 1) Is it supposed to work with .Clear() and then add new items after the first time? 2) Why does it work the first time with adding new items? 3) Am I doing something incorrectly? 4) Why does the example .Clear() and then re-instantiate it? Thanks!

## Answer

**Dimo** answered on 24 Feb 2022

Hello Charles, To detect changes in a component value, we use the default .NET EqualityComparer and Equals () method. By default, this method returns true when comparing the same instance of reference type objects. That's why you need to reset the instance with ToList() or new List() when you change the MultiSelect value programmatically. From this point of view: Why .Clear() if you're going to re-instantiate it? You are right, Clear() is not necessary and you can use only TheValues=new List<int>(); Is it supposed to work with .Clear() and then add new items after the first time? No. Why does it work the first time with adding new items? Generally, such scenarios work when a Razor property instance instance is new, or we sometimes assume new values and execute more code internally to refresh the component state. However, we can't do that always, for performance reasons. Am I doing something incorrectly? From what I see - no. Why does the example .Clear() and then re-instantiate it? This is not necessary and I fixed the example. Changes will go live soon. Regards, Dimo Progress Telerik

### Response

**Charles** commented on 24 Feb 2022

Thanks! Since I posted this, I found a similar situation with an InputSelect. This explains why.
