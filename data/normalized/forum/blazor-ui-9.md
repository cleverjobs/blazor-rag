# Blazor UI 9

## Question

**Dav** asked on 02 Jul 2025

I am seeing a different behavior between Blazor UI 8 and 9. Since upgrading to version 9 the GridToolBarTemplate is getting a k-toolbar-scrollable and the toolbar is getting wrapped in a div with k-toolbar-items k-toolbar-items-scroll classes. This is preventing my toolbar from rendering the way it did in version 8. I added <GridToolBarSettings OverflowMode="GridToolBarOverflowMode.None" /> as he first element of the template but that had no effect. How can I prevent the toolbar from getting this new div and classes? Thanks, Dave Shine dshine@caseglide.com

## Answer

**Hristian Stefanov** answered on 04 Jul 2025

Hi Dave, With the release of Telerik UI for Blazor 9.0.0, the Grid’s toolbar rendering was updated. The content inside the GridToolBar or GridToolBarTemplate is now wrapped in an extra <div> with the k-toolbar-items and k-toolbar-items-scroll classes. This change supports new toolbar features and is now part of the component’s structure. Built-in Options There are no built-in options or settings available to remove or prevent the rendering of this wrapper <div> and its classes. The OverflowMode setting only controls the overflow behavior of the toolbar, not the presence of the wrapper itself. Restoring Previous Appearance To achieve a layout similar to version 8, you can override the styles applied to the new wrapper. For example, you can use CSS to neutralize the effect of the extra <div>: .k-toolbar-items-scroll { /* Adjust or reset styles as needed */ padding: 0; background: none; /* Optionally, use display: contents; to minimize wrapper impact */ display: contents;
} or <style>.k-grid-toolbar.k-toolbar-items { flex-flow: row wrap;
} </style> Overall, you can experiment with these styles until you achieve what you are looking for. Summary The extra <div> and its classes are by design in v9.0.0 and cannot be removed via a built-in setting. Custom CSS is the recommended approach to restore your desired toolbar layout and appearance. Regards, Hristian Stefanov Progress Telerik

### Response

**David** commented on 07 Jul 2025

Thank you Hristian for your response. After some experimentation I found that all I need to do add this style to my site.css file .k-toolbar-items-scroll { display: contents;
}
