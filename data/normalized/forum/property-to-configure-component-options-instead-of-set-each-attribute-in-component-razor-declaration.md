# Property to configure component options instead of set each attribute in component razor declaration

## Question

**Cla** asked on 06 May 2022

It would be glad to add a property in telerik blazor components allow to manage all component settings. This because some components has many attributes and binding to single properties on class is a nightmare. It was done in angular with k-options attribute, in blazor can be for example: <TelerikGrid Data="" Pageable="" PageSize="" Sortable="" Resizable="" Reorderable="" SelectionMode="" EditMode="" OnRead="" OnCreate="" OnUpdate="" OnCancel="">... </TelerikGrid> to <TelerikGrid Options="Options">... </TelerikGrid> @code { private TelerikGridOptions<Model> Options {get;set;} protected override void OnInitialized() { Options=new TelerikGridOptions<Model> { ... }; } }

## Answer

**Marin Bratanov** answered on 07 May 2022

Hello Claudio, In Blazor, the way to do this is to create a component in your app, and put the Telerik component with the desired parameters in it. Thus, you can reuse that custom component and expose on it only a few of the settings you plan to modify/set, and the events you may need (say, ones for two-way binding of parameters). Then you can reuse your custom component by giving its parameters values in any way you desire - be that as separate parameters, be that as some sort of unified collection of settings. Regards, Marin Bratanov
