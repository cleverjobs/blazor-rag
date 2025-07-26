# Bug? Menu with SubItems and CloseOnClick=true never opens in TouchScreens, as there is no Hover

## Question

**Víc** asked on 03 Jul 2023

Hy telerik, On touch screens there is no hover so you need to click an item to open the menu for the children items. This is not taken into account by the current implemnentation of CloseOnClick. Becouse if set to True, it never opens the nested menu items. For now I will set CloseOnClick=false in order to be able to open the submenus. But this will make the menu stay opened after clicking a item. With is a very anoying user experience. I can provide an exemple if necesary. Eveything works as expected on Descktop, as the submenu opens with hover. Is this a bug? Will it be fxed? Is there a way to close the menu programatically? Any workaround? I have no found a duplicate post. Cheers!

## Answer

**Hristian Stefanov** answered on 05 Jul 2023

Hi Víctor, Thank you for sharing such comprehensive information about the scenario. Now let me shed some light on it below. The described Menu behavior is a side effect caused by the browser firing the hover event on a tab/click on the mobile devices screen. Therefore, we have an open feature request that will address your needs and will help you achieve the desired mobile device result: [mobile] Hide child menu items on parent click/tap. I voted there on your behalf and raised the priority. You can also subscribe to it to receive email notifications for status updates. In the meantime, if we come across any potential alternative approaches, I will promptly add them as comments to the item linked above. I remain at your disposal if we can assist with more information. Regards, Hristian Stefanov
