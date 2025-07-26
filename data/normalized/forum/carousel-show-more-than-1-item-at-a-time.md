# Carousel show more than 1 item at a time.

## Question

**Ita** asked on 13 Jan 2022

Hi, Im looking to make a carousel but I would like it to show more than 1 item at once <item1 item2 item3> instead of <item1> and onclick I would get <item2 item3 item4>

## Answer

**Marin Bratanov** answered on 15 Jan 2022

Hello Itamar, The following article explains how to have more than one item in the viewport: [https://docs.telerik.com/blazor-ui/knowledge-base/carousel-more-than-one-item-in-viewport](https://docs.telerik.com/blazor-ui/knowledge-base/carousel-more-than-one-item-in-viewport) Regards, Marin Bratanov

### Response

**Itamar** commented on 16 Jan 2022

Thank you!

### Response

**Itamar** commented on 17 Jan 2022

Is it possible for them to move over 1 at a time instead of all of them at once?

### Response

**Marin Bratanov** commented on 17 Jan 2022

Sadly, no. Effectively, what this does is to still have 1 item in the viewport, but that item's layout contains more data. So it is that "parent" item that moves.
