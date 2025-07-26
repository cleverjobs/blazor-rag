# Remove download option from Context menu of FileManager Blazor

## Question

**Tas** asked on 08 Apr 2025

Hi Team, Is there a way to remove download option from Context menu of FileManager Blazor

## Answer

**Anislav** answered on 08 Apr 2025

I believe the FileManager component does not currently offer a way to customize the context menu. As a workaround, you can hide the Download option using CSS like this: <style> li.k-menu-item:has ( span.k-svg-i-download ) { display: none;
} </style> Keep in mind that this approach may stop working in the future if Telerik removes the Download icon from the context menu. Regards, Anislav Atanasov

### Response

**Anislav** commented on 23 Apr 2025

Did the proposed workaround work for you?
