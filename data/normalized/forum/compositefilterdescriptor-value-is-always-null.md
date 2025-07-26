# CompositeFilterDescriptor Value is always null

## Question

**EE** asked on 21 Oct 2020

I have a Data grid which is populated with remote data 1 page at a time using OnRead. This requires custom sort and filtering in the OnRead method. When I was using filter row, and the filters were returned as FilterDescriptor, and their value was populated. When I changed the setting to filtermenu, and started getting composite filters (which I wanted), the values were always null, regardless of what I entered. Is this the right way to get values from the composite filters? If so, why is the value of each FilterDescriptor always null? if (filter is FilterDescriptor) { FilterDescriptor currFilter=filter as FilterDescriptor; var member=currFilter.Member; var operation=currFilter.Operator; var value=currFilter.Value; //value is not null } else if(filter is CompositeFilterDescriptor) { var filters=filter as CompositeFilterDescriptor; foreach (var compFilter in filters.FilterDescriptors) { FilterDescriptor currFilter=compFilter as FilterDescriptor; var member=currFilter.Member; var operation=currFilter.Operator; var value=currFilter.Value; //value is always null } }

## Answer

**Svetoslav Dimitrov** answered on 22 Oct 2020

Hello Erin, We have an open bug report regarding the behavior you are experiencing. You can see it from here. I have given your Vote for it and you can Follow it to receive email notifications on status updates. The workaround I could suggest for the time being would be to swap the FilterMode to FilterRow. Regards, Svetoslav Dimitrov
