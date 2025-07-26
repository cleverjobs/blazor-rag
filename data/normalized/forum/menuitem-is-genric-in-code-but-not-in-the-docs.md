# MenuItem is genric in code but not in the docs

## Question

**Nat** asked on 25 Jan 2024

Hi I want to use the TelerikMenu so I'm trying to create a list of menu items to pass to the Data property <TelerikMenu Data=menuItems> </TelerikMenu> List<MenuItem> menuItems; and I'm getting an error: "Using the generic type 'MenuItem<TItem>' requires 1 type arguments" but in the docs, I see it'd be used without a generic parameter: [https://docs.telerik.com/blazor-ui/components/menu/overview](https://docs.telerik.com/blazor-ui/components/menu/overview) Thanks

### Response

**Jay** commented on 30 Jan 2024

Ran into this as well. You need to define a MenuItem class explained here: [https://docs.telerik.com/blazor-ui/components/menu/data-binding/overview](https://docs.telerik.com/blazor-ui/components/menu/data-binding/overview)
