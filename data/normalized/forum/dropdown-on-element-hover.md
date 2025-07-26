# Dropdown on element hover

## Question

**Boh** asked on 24 Mar 2025

Hi! I wanted to ask if it's possible to create a menu similar to the one you have on your main website ([https://www.telerik.com),](https://www.telerik.com),) using Telerik UI for Blazor components? I'm specifically referring to the menu that appears on hover — where a dropdown with multiple columns and grouped content is shown. I've already built a working version of this using AnimationContainer and some custom hover logic, but I'm wondering if there's a simpler or more "official" way to achieve the same effect using Telerik components out of the box? Image is attached. Thanks, appreciate your help! Bohdan

## Answer

**Anislav** answered on 24 Mar 2025

Hi There isn't a built-in component that fully matches your requirements. The closest option is the Menu component, but it functions more like a context menu and lacks built-in header and footer templates for further customization. That said, the Menu component internally relies on the Popup component. Given this, you might consider using the Popup instead of the AnimationContainer. The Popup component represents an animated container that displays in relation to a specific anchor element (e.g., a menu link). In contrast, the AnimationContainer component is primarily designed for creating messages, expandable containers, or popups :) The Popup component was introduced more recently in version 5.1.0 (released on January 31, 2024), which may explain the relatively fewer examples available for it. However, based on its features, it seems like a better option for your use case compared to the AnimationContainer. Regards, Anislav Atanasov

### Response

**Bohdan** commented on 24 Mar 2025

Anislav Atanasov, thank you for your quick response! Regards, Bohdan
