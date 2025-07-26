# Hierarchical Drawer Mini mode active

## Question

**Mar** asked on 10 Apr 2025

Hy, I'm using a hierarchical drawer following the example: Blazor Drawer Demos - Hierarchical Drawer | Telerik UI for Blazor If I activate the mini mode the hierarchical drawer appears as follows: Is there something in the component where the drawer in mini mode displays all the items of the next levels in a popup that opens and closes when the cursor goes over the item at level 0? As the picture below Thanks

## Answer

**Anislav** answered on 13 Apr 2025

No, there isn’t a built-in feature for that specific behavior. However, as demonstrated in the example you shared, the Drawer component is highly customizable, so you should be able to implement this functionality yourself. Just keep in mind that mobile devices don’t support mouseover interactions, so it’s important to ensure that nested items remain accessible—perhaps by allowing the drawer to expand on click. Regards, Anislav Atanasov
