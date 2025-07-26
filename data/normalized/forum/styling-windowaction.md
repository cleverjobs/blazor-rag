# Styling WindowAction

## Question

**aeh** asked on 22 Jan 2021

With the release of 2.21 we can apply styles to the windows elements, and that is great! How can we apply these styles to the WindowAction elements?

## Answer

**Marin Bratanov** answered on 22 Jan 2021

Hi, You can customize them through CSS cascading through the parent class in case the built-in settings don't suffice for you: [https://docs.telerik.com/blazor-ui/components/window/actions.](https://docs.telerik.com/blazor-ui/components/window/actions.) For example: <style>.my-custom-actions.k-window-titlebar button { border: 2px solid blue!important; background: yellow!important; color: green!important;
} </style> <TelerikWindow Visible="true" Class="my-custom-actions"> <WindowActions> <WindowAction Name="MyAction" Icon="gear" /> <WindowAction Name="Close" /> </WindowActions> <WindowTitle> Optional title </WindowTitle> <WindowContent> lorem ipsum </WindowContent> </TelerikWindow> Regards, Marin Bratanov
