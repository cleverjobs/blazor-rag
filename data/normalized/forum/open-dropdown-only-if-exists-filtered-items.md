# Open dropdown only if exists filtered items

## Question

**And** asked on 12 Oct 2023

Hi, in a combobox with filter and custom values, if user start typing and there are no items corresponding to the filter the dropdown is open also if it is empty. Is it possibile to avoid this and open dropdown only if there are items? PS. Also Autocomplete component have same behaviour Thank you

## Answer

**Dimo** answered on 12 Oct 2023

Hello Andrea, By design, the dropdown opens before the filtered data is received, so we don't know if there are results or not. We believe this approach is better in terms of faster component operation and user experience. If the dropdown doesn't open, the user may think that they need to type the whole (existing) value on their own. Regards, Dimo Progress Telerik

### Response

**Andrea** commented on 12 Oct 2023

Thank you, I understand what you say and I think that for desktop is ok, but in mobile (smartphone), in my opinion, open an empty dropdown that hide other controls also if there are not items, can be a little bit confusing for user specially if he want to type a new value. Thank you for explanation. Best regards, Andrea
