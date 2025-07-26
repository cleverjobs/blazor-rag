# Sass ThemeBuilder

## Question

**Mat** asked on 28 Oct 2021

I had to search for a while and found nothing about this. For those who need to use ThemeBuilder for the import: The json file must be adjusted before: from "base": "@progress/kendo-theme-default", "product": "kendo", "components": [], "themeBuilder": [
{ to "base": "@progress/kendo-theme-default", "product": "kendo", "components": [], "groups": [
{ Best regards Matthias

### Response

**Ivan Zhekov** commented on 01 Nov 2021

Hey, Mathias. The change was intended to serve as an improvement by switching a specific "themeBuilder" field to a much more generic "groups". We did support both syntax variants for a while for import and then exported only groups syntax. Finally we made the switch to groups. That being said, the syntax is not expected to change anytime soon, because it doesn't get much more generic than that. We could add a version field to somewhat denote which version should be used or to facilitate transition, but that's adding new things, not changing existing.

### Response

**Matthias** commented on 01 Nov 2021

Thank you for the explanation. I had only wondered that after the import in ThemeBuilder no more colors were visible. But after exporting as JSON from there, it quickly became clear that this was just this entry. Before someone has to search longer, I thought that this info is well kept in the forum. have a nice start of the week! Best regards
