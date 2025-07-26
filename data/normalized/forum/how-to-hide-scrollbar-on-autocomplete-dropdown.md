# How to hide scrollbar on AutoComplete dropdown?

## Question

**Phi** asked on 07 Feb 2023

Hi Im using the autocomplete component and I want to hide the scrollbar from the popup that displays the results but I don't know which class to modify to set overflow: hidden Can anyone help? Thanks

## Answer

**Nadezhda Tacheva** answered on 10 Feb 2023

Hi Phil, By design, the webkit-scrollbar will appear if the AutoComplete popup height is not enough to display all items. If you want to have a non-scrollable popup, you may adjust its height, so it fits all items. This can be configured through the popup settings. In case you want to keep the scrolling functionality but simply hide the scrollbar, you may target the webkit-scrollbar of the k-list-scroller element and apply styles like the ones listed here: [https://stackoverflow.com/questions/16670931/hide-scroll-bar-but-while-still-being-able-to-scroll/38994837#38994837.](https://stackoverflow.com/questions/16670931/hide-scroll-bar-but-while-still-being-able-to-scroll/38994837#38994837.) In this scenario, I would also recommend setting a custom class to the popup to ensure you are targeting this specific popup element. Here is a runnable sample demonstrating thе approach: [https://blazorrepl.telerik.com/wducvuEX0458Z4Xs14.](https://blazorrepl.telerik.com/wducvuEX0458Z4Xs14.) I hope you will find this information and example useful. Should you have any further questions, please do not hesitate to reach out. Regards, Nadezhda Tacheva
