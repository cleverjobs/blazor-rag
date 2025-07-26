# New errors after updating to Visual Studio 2022 version 17.3 preview 1.0

## Question

**Zac** asked on 12 May 2022

Started seeing errors after updated V.S. Pages that uses TelerikGrid has these 2 errors. It compiles fine and run fine, so i'm not sure how to fix. Error (active) CS1503 Argument 2: cannot convert from 'Microsoft.AspNetCore.Components.EventCallback<System.Collections.Generic.IEnumerable<mymodel>>' to Microsoft.AspNetCore.Components.EventCallback' Error (active) CS0246 The type or namespace name 'TItem' could not be found (are you missing a using directive or an assembly reference?) Please advise Thanks, ZB

### Response

**Dimo** commented on 17 May 2022

Hi Zack, This error suggests an event handler with an incorrect argument type. However, the screenshot does not point which one. Can you provide an example? On the other hand, if the app compiles and runs fine, then maybe Visual Studio got confused in some way. Sometimes these errors disappear after a Visual Studio restart.
