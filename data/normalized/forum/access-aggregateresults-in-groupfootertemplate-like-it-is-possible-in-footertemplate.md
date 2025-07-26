# Access AggregateResults in GroupFooterTemplate like it is possible in FooterTemplate

## Question

**Kat** asked on 01 Apr 2022

Hi, I need to calculate a grouping value by myself as the standard GridAggregateTypes are not suitable in my case (I need to calculate a percentage based on the aggregated values of other columns in the same grouping). This is possible for the GridFooterTemplate as the GridGroupTemplateContext provides the AggregateResults from which I can calculate the value to be shown. However, the GridGroupTemplateContext provided by the GroupFooterTemplate does not provide such a property. Any kind of solution is helpful, even if it is a dirty workaround. Thank you very much and best regards - Richard

## Answer

**Nadezhda Tacheva** answered on 06 Apr 2022

Hi Richard, Indeed, the GroupFooterTemplate context currently does not expose the aggregate results of all Grid data. It allows to only aggregate the current field. However, we do have a feature request to expose aggregates for all the fields in the Group Header and Footer templates. I have added your vote to increase its popularity as we are prioritizing the feature requests implementation based on the community interest and demand. You can follow the item, so you are notified via email on its status updates. I am afraid that at this stage there is not an easy and stable way that we would recommend to let the GroupFooterTemplate of a column access and use aggregates of other columns. If this functionality is urgent for you, we have a Feature Acceleration Program which allows you to negotiate a deal with our management to include the feature sooner in our roadmap. This service is paid. Please let me know if you'd be interested in that, so I can put you in touch with our Professional Services team to discuss it. Regards, Nadezhda Tacheva
