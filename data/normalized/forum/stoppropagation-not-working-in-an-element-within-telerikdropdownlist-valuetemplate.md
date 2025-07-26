# stopPropagation not working in an element within TelerikDropDownList ValueTemplate

## Question

**Fab** asked on 30 Sep 2021

I've created a component for picking a sorting field, that consists in a TelerikDropDownList where I've added a button with an icon to specify the sorting order something like this <TelerikDropDownList Value="_sortingValue.Value" Data="Choices" PopupHeight="auto" PopupWidth="200px" Class="max-w-min flex-grow" ValueChanged="@((TEnum sorting)=> OnSortChanged(sorting))"> <ItemTemplate> @ValueTranslator(context) </ItemTemplate> <ValueTemplate> <div class="flex flex-row items-center"> <button class="flex items-center text-primary p-2 hover:text-secondary" @onclick="()=> OnChangeOrder(_sortingValue.Order)" @onclick:stopPropagation="true"> <Icon> @GetSortIcon(_sortingValue.Order) </Icon> </button> <div> @ValueTranslator(context) </div> </div> </ValueTemplate> What I want to do is being able to click the sorting icon without causing the DDL to open I tried adding @onclick:stopPropagation="true on the button but it doesn't work. Is like if you have some kind of javascript that register a click on any item within the ValueTemplate and it causes the drop down list to open ignoring my stopPropagation Can you help me solve the problem? Thanks

## Answer

**Dimo** answered on 05 Oct 2021

Hi Fabio, Indeed, opening the dropdown cannot be prevented from inside the ValueTemplate. If possible, please consider moving the sorting button outside the DropDownList or inside its HeaderTemplate. On the other hand, you can mimic the DropDownList behavior with a TelerikButton (or any HTML markup) that opens an AnimationContainer with the item list. However, this is a more complex option to implement, so I hope the first two alternatives are feasible. Regards, Dimo Progress Telerik
