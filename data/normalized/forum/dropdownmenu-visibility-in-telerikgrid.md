# DropDownMenu visibility in TelerikGrid

## Question

**Ann** asked on 04 Mar 2021

I'm using TelerikGrid. In first Column in every row I have button and when customer press button dropdownmenu is opening. But if there is few rows in grid, DropDownMenu is not showing properly, it's behind the grid I tried to add this, but it didn't help. td[role=gridcell] { overflow: visible !important; color: #6f717a; }

## Answer

**Nadezhda Tacheva** answered on 05 Mar 2021

Hello Anna, The reason for this behavior most likely stems from the dropdown position in the DOM. When dealing with Grid, the positioning of such items can be complicated as the component itself has pretty complicated structure. To validate what styles are computed on the dropdown, you may check the dev tools in your browser. As for the purposes of achieving your desired scenario, you might consider the following feature requests that we have opened in our
