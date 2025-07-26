# use Popover in Telerik Map for Blazor

## Question

**Lin** asked on 27 Apr 2025

Hi Please guide me how can I use Popover in the Map instead of showing Tooltip?

## Answer

**Anislav** answered on 27 Apr 2025

Based on the image you attached, I assume you would like to display a button inside the map's tooltip. While this is technically possible, it is not practical, as the tooltip will disappear as soon as the mouse leaves the marker, preventing users from clicking the button. There is already a similar feature request — Show marker tooltip on click instead of on hover — but it is currently not planned for implementation by Progress. At the moment, it is not possible to customize the Map to change its behavior for displaying tooltips on hover. However, as a workaround, you can handle the OnMarkerClick event and display the additional information, including a button, either next to the map or inside a separate window. I have prepared a sample demonstrating one of these workarounds: [https://blazorrepl.telerik.com/wzYomrlG25wuXaBY56](https://blazorrepl.telerik.com/wzYomrlG25wuXaBY56) Regards, Anislav Atanasov
