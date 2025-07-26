# How does the Tabstrip PersistContent know a tab already exists

## Question

**And** asked on 03 May 2022

I have a Tabstrip with several open "documents" as tabs and I've provided the user the option to "reload" the document, or discard changes. I remove my model object from the list of open tabs and re-add a new instance of that object, however the tabstrip doesn't see this as a new instance and therefore remains with the older rendering. If on the other hand I remove my object, call StateHasChange, then re-add the object and call StateHasChanged again my object is re-rendered correctly. This behavior is not ideal though, is there a way to inform the tabstrip that the instance of the object that represents this tab has changed? Thanks -Andy

## Answer

**Andrew** answered on 04 May 2022

The answer to this question is to use the magic @key attribute which Blazor uses to determine if something is new (and needs rendering) or not. By adding an @key attribute to the content of my tab, I was able to remove and re-insert an item in the list which on the surface looked similar, but was actually a different instance. Since my generated key for this instance was different, Blazor picked up the change. <Content> <JobView JobEditItem="@jobEditItem" @key="@jobEditItem.UniqueId" /> </Content> -Andy

### Response

**Joana** answered on 06 May 2022

Hi Andrew, Indeed, as you have mentioned already, it is not really up to the TabStrip itself to decide when to rerender or not the content of a given tab, rather than the framework itself. When rendering items in a loop, @key guarantees that an element will not be re-rendered if the value of the key has not changed, or will re-render(as desired in your case) if it has changed. Regards, Joana
