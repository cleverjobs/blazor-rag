# How to control DropDownList to not auto select values as you navigate the list via keyboard

## Question

**Rev** asked on 19 May 2025

I currently have a case to where I have a DropDownList with a ValueChange(), depending on which one the user chooses, I need to throw a popup for confirmation. As the user 'scrolls' through the options with the arrow keys, this will cause that popup to be selected. Outside of this, we do not like the idea of when pressing ESC, the last highlighted value is kept. Is there any native control to change this? We have a lame workaround but it is highly desired to have the ability to limit a selection by the ENTER key. As far as we know, this 'style' should be 508 compliant. Ex DropDownList: <TelerikDropDownList Value="@cart.brand" Id="brand_dropdown" Data="@Organizations" ValueField="Name" TextField="Name" DefaultText=" " Width="100%" TValue="string" TItem="BrandViewModel" ValueExpression="@(()=> cart.brand)" ValueChanged="@((e)=> HandleSelectBrand(e))"> </TelerikDropDownList>
