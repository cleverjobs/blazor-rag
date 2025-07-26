# Missing CSS rule using Theme Builder

## Question

**Twa** asked on 15 Mar 2023

I just generated a new theme using Theme Builder and detected that the " k-align-items-baseline " rule is not included. This generates backward incompatibility although it is easily fixable. My question is if this is intentional or a bug. Can I expect other styles to be missing as well? Regards.

### Response

**Radoslav** commented on 20 Mar 2023

Hi Twain, Can you elaborate a bit more on your scenario? From which component is the mentioned CSS class and which style from the ThemeBuilder is not applied or overridden? In general, the ThemeBuilder generates the styles with selectors that are with bigger weight than the selectors in the Kendo Themes, thus the styles from the ThemeBuilder can override the styles from the themes. Looking forward to your reply.
