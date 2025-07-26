# Disabled state for items

## Question

**Kas** asked on 25 Jun 2020

Hi, can specific items in the DropDownList be disabled? I.e. non-selectable and visually marked as disabled? Scenario: we sometimes face the issue of having obsolete objects being referenced. Those obsolete objects may be marked as "deleted" in the database but are still referenced and need to be displayed if already referenced, but are not allowed to be selected anymore. How would one do this with Blazor and Telerik's components? Regards Kasimier Buchcik

## Answer

**Svetoslav Dimitrov** answered on 25 Jun 2020

Hello Kasimier, Currently, what I can suggest is you filter them out or remove them from the data source. As attached file, you can see a demo which shows how to visually show that those items are not available by using the ItemTemplate, but selecting them would still be available using the keyboard navigation, however they would not be clickable with the mouse. Would you expect our component to provide such feature out of the box and what the API of it would be? For example, you could provide a collection of items to be disabled or something else? I would appreciate your input on the matter. Regards, Svetoslav Dimitrov

### Response

**Kasimier Buchcik** answered on 29 Jun 2020

[quote]Would you expect our component to provide such feature out of the box.[/quote] Yes, I would be nice if at least the features of HTML's select/option were available. (Which could also mean support for an optgroup) [quote]and what the API of it would be?[/quote] I guess a "DisabledField" parameter would fit the existing API (because there is a "ValueField" and "TextField"). But I can imagine that this all will be a source of endless requests and frustration if one cannot take control of everything explicitly if needed. I.e. will we be able to do the following someday? Pseudo-code: <DD> <Item [bindings, style]/> <ItemsGroup [style]> @foreach (var item in SomeItems) { <Item [bindings, style]> } </ItemsGroup> <ItemsGroup [style]> @foreach (var item in OtherItems) { <Item [bindings, style]> } </ItemsGroup> </DD> Regards Kasimier Buchcik

### Response

**Svetoslav Dimitrov** answered on 29 Jun 2020

Hello Kasimier, Thank you for your valuable feedback on those questions. I would like to follow up with one regarding what you would expect as an user of the component. The DisabledItems (or any name of the parameter) should be a collection of items, which the component will internally iterate and compare against the entire collection passed to the DropDownList. All of the items in the collection to be disabled must be in the main collection too, is this the behavior you expect? What would be the thing you expect to happen if one of the items is not present in the main collection? It would be valuable if you could provide some insights from the point of view of the consumer of the component. After our discussion I would offer a summary and open a Feature Request based on the information. Regards, Svetoslav Dimitrov

### Response

**Kasimier Buchcik** answered on 30 Jun 2020

I guess a "DisabledField" parameter would fit the existing API. From my experience such soft-deleted objects either have a boolean flag and/or a timestamp that indicates a soft-deletion. Never had a scenario where I needed a "DisabledItems" list because the soft-deletion information was always sitting on the object itself. That also why I try to avoid primitive data types (like enums) because I can't soft-delete those without headaches. May I ask how the idea of a "DisabledItems" collection came to life? Because you thought of a collection of objects of primitive data type like strings or enums?

### Response

**Kasimier Buchcik** answered on 30 Jun 2020

I shouldn't have used the term "primitive data type". But I assume you know what I mean: If one is implementing support for soft-deleted objects then one should assume that those objects are of complex type and hold information about being marked as soft-deleted. Generally I would be less anxious if Telerik's Blazor components were implemented with a "complex type object" first philosophy in mind. Same for the examples. When I look at an example which operates on a list of strings only (again), then a part of me starts to weep, because I think: did they think about the other scenarios too, or will I become frustrated in the future?

### Response

**Svetoslav Dimitrov** answered on 30 Jun 2020

Hello Kasimier, I am opening a Feature Request on our Feedback Portal, which you can see from this link. I have given a Vote on your behalf and you can Follow it for email notifications on status updates. That being said, providing support for disabled items for the DDL (or other similar components like Combobox) we should think of more generic approach rather than only support for soft-deleted items that carry a flag or other marker. We should rather consider providing such feature for limiting user access to the website, perhaps even for location based disabled items (for example some website features are not available for certain geo-locations based on Localization), etc. Regards, Svetoslav Dimitrov

### Response

**Kasimier Buchcik** answered on 01 Jul 2020

Please remove my name from the request you opened. Please don't write stuff on my behalf and put my name on it in the future. Thank you.

### Response

**Svetoslav Dimitrov** answered on 01 Jul 2020

Hello Kasimier, I have opened a new Feature Request on my behalf and deleted the one I created on your. You can see it (and Follow it) from here. I have added your Vote for it. On a side note I would like to mention that this too is a public forum, not only the Feedback Portal. Regards, Svetoslav Dimitrov

### Response

**Kasimier Buchcik** answered on 01 Jul 2020

[quote]On a side note I would like to mention that this too is a public forum, not only the Feedback Portal.[/quote] My concern was not with posts being public, my concern is with Telerik's staff writing stuff on someone's behalf without even asking for permission.

### Response

**Dimo** answered on 02 Jul 2020

Hello Kasimer, Please accept our apologies for making you feel uncomfortable. When logging feature requests or bug reports on customers' behalf, our goal is to spare them the need to do that on their own and basically rewrite their support ticket or forum post in a different place. Another benefit is that the given customer becomes automatically subscribed for updates. Thanks for your honest feedback! Regards, Dimo

### Response

**Kasimier Buchcik** answered on 02 Jul 2020

Hi, everything's fine. Someone wrote, I asked to change it, issue's fixed. But for other folks in the future everything could be even finer if: 1) one would be asked for permission beforehand 2) it would be clearly visible in those requests/reports who wrote what 3) the original discussion would be included at least as a link Regards Kasimier Buchcik

### Response

**Dimo** answered on 02 Jul 2020

Hi Kasimer, Thank you for the additional suggestions! They are surely reasonable and we will take them into account when considering how to improve our processes. Regards, Dimo
