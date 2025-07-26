# menu popup

## Question

**kha** asked on 15 Jun 2020

Hello, how is it possible to change styles and template of popup which open under menu OnHover ?

## Answer

**Marin Bratanov** answered on 16 Jun 2020

Hello Khashayar, You can add logic (say, if-else blocks) in the Template of the menu to know what to render depending on your business needs. A similar example is available in our documentation: [https://docs.telerik.com/blazor-ui/components/menu/templates.](https://docs.telerik.com/blazor-ui/components/menu/templates.) For example, in your case you could have a flag that denotes root items and check for that. You may also find interesting and relevant this thread and the feature request it points to: [https://www.telerik.com/forums/is-there-a-way-to-have-a-sub-item-template](https://www.telerik.com/forums/is-there-a-way-to-have-a-sub-item-template) Regards, Marin Bratanov
