# AutoFit all Columns on TelerikGrid Mis-Aligns the NavMenu.

## Question

**Pet** asked on 04 Sep 2024

Hello Telerik, When I first generator the Grid the menu appears as expected. When I AutoFit All Columns the NavMenu is mis-alligned. Thank you

## Answer

**Dimo** answered on 04 Sep 2024

Hello Peter, You are experiencing an issue that is related to CSS and browser behavior. The Grid will require an absolute Width value in this case. It can be in pixels, viewport units, or anything other than percent. The other option is to rework the app layout, so that it's not based on CSS flexbox. Regards, Dimo Progress Telerik
