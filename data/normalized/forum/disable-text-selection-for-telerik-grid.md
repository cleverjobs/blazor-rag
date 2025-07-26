# Disable text selection for telerik grid

## Question

**Ant** asked on 19 Jun 2023

Is there a way to disable text selection. I tried adding this css class .disable-selection { user-select: none; } on the <TelerikGrid/> level but I can still highlight text.

## Answer

**Anthony** answered on 19 Jun 2023

Feeling a little stupid I just had to wrap it in a div. <div class="disable-selection> <TelerikGrid ..../> </div>
