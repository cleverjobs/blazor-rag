# Using Open Iconic fonts in DrawerItem??

## Question

**Jst** asked on 23 Jun 2022

I would like to use the Open Iconic font icons in the drawer element instead of the default Telerik icons. I can get the css class to reflect the classes for the icons but the component insists on also adding the k-icon & k-i- classes into the class section of the before span. The k-icon class and k-i- partial class name override the oi & oi-flag class I specify. How do I use the Open Iconic fonts in the DrawerItem section?

## Answer

**Dimo** answered on 28 Jun 2022

Hello John, The Drawer will "insist" :) only if you are using Icon and IconField. Instead, use IconClass and IconClassField. Also check the Drawer Icons documentation. Another option for your case is to use the Drawer Template, but that is necessary only if you need full control over the HTML output. Regards, Dimo
