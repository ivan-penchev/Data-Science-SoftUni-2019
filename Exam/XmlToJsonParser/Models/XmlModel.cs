   /* 
    Licensed under the Apache License, Version 2.0
    
    http://www.apache.org/licenses/LICENSE-2.0
    */
using System;
using System.Xml.Serialization;
using System.Collections.Generic;
namespace XmlModel
{
	[XmlRoot(ElementName="modification", Namespace="http://www.auto-data.net/")]
	public class Modification {
		[XmlElement(ElementName="id", Namespace="http://www.auto-data.net/")]
		public string Id { get; set; }
		[XmlElement(ElementName="update", Namespace="http://www.auto-data.net/")]
		public string Update { get; set; }
		[XmlElement(ElementName="brand", Namespace="http://www.auto-data.net/")]
		public string Brand { get; set; }
		[XmlElement(ElementName="model", Namespace="http://www.auto-data.net/")]
		public string Model { get; set; }
		[XmlElement(ElementName="generation", Namespace="http://www.auto-data.net/")]
		public string Generation { get; set; }
		[XmlElement(ElementName="engine", Namespace="http://www.auto-data.net/")]
		public string Engine { get; set; }
		[XmlElement(ElementName="yearstart", Namespace="http://www.auto-data.net/")]
		public string Yearstart { get; set; }
		[XmlElement(ElementName="yearstop", Namespace="http://www.auto-data.net/")]
		public string Yearstop { get; set; }
		[XmlElement(ElementName="fuelConsumptionUrban", Namespace="http://www.auto-data.net/")]
		public string FuelConsumptionUrban { get; set; }
		[XmlElement(ElementName="fuelConsumptionUrbanMin", Namespace="http://www.auto-data.net/")]
		public string FuelConsumptionUrbanMin { get; set; }
		[XmlElement(ElementName="fuelConsumptionCombined", Namespace="http://www.auto-data.net/")]
		public string FuelConsumptionCombined { get; set; }
		[XmlElement(ElementName="fuelConsumptionCombinedMin", Namespace="http://www.auto-data.net/")]
		public string FuelConsumptionCombinedMin { get; set; }
	}

	[XmlRoot(ElementName="modifications", Namespace="http://www.auto-data.net/")]
	public class Modifications {
		[XmlElement(ElementName="modification", Namespace="http://www.auto-data.net/")]
		public List<Modification> Modification { get; set; }
	}

	[XmlRoot(ElementName="generation", Namespace="http://www.auto-data.net/")]
	public class Generation {
		[XmlElement(ElementName="name", Namespace="http://www.auto-data.net/")]
		public string Name { get; set; }
		[XmlElement(ElementName="id", Namespace="http://www.auto-data.net/")]
		public string Id { get; set; }
		[XmlElement(ElementName="modifications", Namespace="http://www.auto-data.net/")]
		public Modifications Modifications { get; set; }
	}

	[XmlRoot(ElementName="generations", Namespace="http://www.auto-data.net/")]
	public class Generations {
		[XmlElement(ElementName="generation", Namespace="http://www.auto-data.net/")]
		public List<Generation> Generation { get; set; }
	}

	[XmlRoot(ElementName="model", Namespace="http://www.auto-data.net/")]
	public class Model {
		[XmlElement(ElementName="name", Namespace="http://www.auto-data.net/")]
		public string Name { get; set; }
		[XmlElement(ElementName="id", Namespace="http://www.auto-data.net/")]
		public string Id { get; set; }
		[XmlElement(ElementName="generations", Namespace="http://www.auto-data.net/")]
		public Generations Generations { get; set; }
	}

	[XmlRoot(ElementName="models", Namespace="http://www.auto-data.net/")]
	public class Models {
		[XmlElement(ElementName="model", Namespace="http://www.auto-data.net/")]
		public List<Model> Model { get; set; }
	}

	[XmlRoot(ElementName="brand", Namespace="http://www.auto-data.net/")]
	public class Brand {
		[XmlElement(ElementName="name", Namespace="http://www.auto-data.net/")]
		public string Name { get; set; }
		[XmlElement(ElementName="id", Namespace="http://www.auto-data.net/")]
		public string Id { get; set; }
		[XmlElement(ElementName="models", Namespace="http://www.auto-data.net/")]
		public Models Models { get; set; }
	}

	[XmlRoot(ElementName="brands", Namespace="http://www.auto-data.net/")]
	public class Brands {
		[XmlElement(ElementName="brand", Namespace="http://www.auto-data.net/")]
		public List<Brand> Brand { get; set; }
		[XmlAttribute(AttributeName="xmlns")]
		public string Xmlns { get; set; }
	}

}
