# Style Separator in Submenu

## Question

**Hen** asked on 02 Dec 2022

I know how to style the horizontal separator like this: .horizontal> .k-separator {
margin: 0;
background-color: #0062cc !important;
} but I can not figure out how to do it for the vertical separators in a submenu. I have problems to inspect the submenu because it closes itself if I try to inspect it (maybe I need a trick here too...)

### Response

**Lisa** commented on 02 Dec 2022

Check this: [https://stackoverflow.com/questions/64456886/emulate-a-focused-page-option-not-available-in-chrome-developer-tools](https://stackoverflow.com/questions/64456886/emulate-a-focused-page-option-not-available-in-chrome-developer-tools) In chrome dev tool you can set “Emulate a focused page”. This will keep the submenu open, when you inspect it. Hope this helps :-)

## Answer

**Hendrik** answered on 03 Dec 2022

Thank you for your time. I followed the link and set the "Emulate a focused page" but the menu was still disappearing. Maybe I got something wrong. But then I found the trick that did it: when the menu is open use Ctrl+Shift+C to focus the element. Now I found my style: .k-menu-group .k-separator {
margin: 0;
background-color: #0062cc !important;
}
