# Composite filter descriptor to find records that match two different columns.

## Question

**Joh** asked on 13 Aug 2024

I'm trying to create filter that works on two columns. The first column "IsActive"=true works properly. I need to have a second filter on a column that filters for all " ParticipantI d" t hat is a nullable integer type thatis either null or empty. Logical this would be an And Currently this is what I have but it does not work. How would I includea filter for a null integer column using AND logic? var filterDescriptors=new List<IFilterDescriptor>
{ new CompositeFilterDescriptor{
FilterDescriptors=[ new FilterDescriptor{
Member="IsActive",
Operator=FilterOperator.IsEqualTo,
Value=true,
MemberType=typeof ( bool )
}, new FilterDescriptor{
Member="ParticipantId",
Operator=FilterOperator.IsNullOrEmpty,
Value=null,
MemberType=typeof ( int )
}
]
}
};

## Answer

**Dimo** answered on 14 Aug 2024

Hello John, There are a few things to fix in the code: There must be a separate CompositeFilterDescriptor for each column. IsNullOrEmpty is not a valid operator for int?. Use IsNull instead. It's better to use nameof () instead of hard-coded strings for the Member property. [https://blazorrepl.telerik.com/coEMbSbR38wk1Rsb34](https://blazorrepl.telerik.com/coEMbSbR38wk1Rsb34) Regards, Dimo
