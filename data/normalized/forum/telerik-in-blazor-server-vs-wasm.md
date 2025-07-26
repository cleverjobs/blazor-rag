# Telerik in Blazor Server vs WASM

## Question

**che** asked on 17 Aug 2021

Hello, This v2.26.0 drop down: <div class="flex-child"> <label for="warehouse" class="k-label k-form-label"> Warehouse </label> <TelerikDropDownList Data="@Warehouses" DefaultText="Select a Warehouse" Id="warehouse" TextField="WarehouseName" ValueField="WarehouseId" ValueChanged="@((int w)=> WarehouseSelected(w))" /> </div> ...is working in a Blazor WASM app (well, I'm having issues overriding css classes used by Telerik controls, but that's another topic). Here it is, working OK in Blazor WASM: However, using the same code in a Razor component in a Blazor-Server project, I am not getting the control rendered properly: I have your script declared in the head part of _Host.cshtml (see below). I'm really not sure about this, and I have moved it around , removed "defer", deleted bin and obj folders and cleared the cache, but to no avail. <head> <meta charset="utf-8" /> <meta name="viewport" content="width=device-width, initial-scale=1.0" /> <title> CalendarDemo.UI </title> <base href="~/" /> <link rel="stylesheet" href="css/bootstrap/bootstrap.min.css" /> <link href="css/site.css" rel="stylesheet" /> <link href="CalendarDemo.UI.styles.css" rel="stylesheet" /> <link href="css/CustomStyles.css" rel="stylesheet" /> <script src="_content/Telerik.UI.for.Blazor/js/telerik-blazor.js" defer> </script> </head> Looking at the dev tools, I do see the above script is making it to the page: This is a mystery to me so far. I am not seeing any exceptions being raised. Any suggestions for further troubleshooting? Thanks again!

## Answer

**Matthias** answered on 17 Aug 2021

In the example I can't see the styleSheet <link rel="stylesheet" href="_content/Telerik.UI.for.Blazor/css/kendo-theme-default/all.css" /> Or is this one:? <link href="css/CustomStyles.css" rel="stylesheet" /> Because the result looks like the stylesheet is not included correctly

### Response

**chesk345** commented on 17 Aug 2021

I think you're right, Matthias. Selecting the listbox in the DOM explorer, I see neither the Kendo nor or my custom CSS being applied: In the Network log, I see my Custom CSS but not Kendo "all.css":

### Response

**chesk345** commented on 18 Aug 2021

My problem was that I did not have the link to all.css in _Host.cshtml. This is the first time I've tried a Blazor Server app, so it was my oversight.
