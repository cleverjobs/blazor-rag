# bind blazor menu to remote data

## Question

**Mil** asked on 19 May 2022

Hello, I have menu table in my database, which have menuid and parentmenuid columns. I want to bind data retrieved from this table to blazor menu. Is it possible ? there is no example showing how to bind blazor menu to remote data. Thanks, Milind Shevade

## Answer

**Marin Bratanov** answered on 22 May 2022

Hello Milind, Our components require that you provide them with a Data collection to render. Where, when and how this data is obtained is in full control of the app. So, you could, for example, start with an empty collection, populate it as needed (say, in OnInitializedAsync), and just set it to the view-model that the menu is bound to. Regards, Marin Bratanov Progress Telerik
