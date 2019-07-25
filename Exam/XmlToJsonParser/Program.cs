using System;
using System.IO;
using System.Text;
using System.Xml.Serialization;


namespace XmlToJsonParser
{
    class Program
    {
        static void Main(string[] args)
        {
            string xmlString =  System.IO.File.ReadAllText("car_efficiency.xml");

            XmlSerializer serializer = new XmlSerializer(typeof(XmlModel.Brands));
            StringBuilder strBld = new StringBuilder();
            using (TextReader reader = new StringReader(xmlString))
            {
                string header = "carBrand,carModel,carModelGeneration,engine,yearStart,yearStop,fuelConsumptionUrban,fuelConsumptionUrbanMin,fuelConsumptionCombined,fuelConsumptionCombinedMin";
                strBld.AppendLine(header);
                XmlModel.Brands result = (XmlModel.Brands)serializer.Deserialize(reader);
                foreach (var brand in result.Brand)
                {
                    string brandName = "unknown";
                    brandName=brand.Name;
                    if(brandName.Contains('-')){
                        brandName=brandName.Replace("-", string.Empty);
                    }
                    if(brandName.Contains(" ")){
                        brandName=brandName.Replace(" ", string.Empty);
                    }
                
                    foreach (var model in brand.Models.Model)
                    {
                        foreach (var modelGen in model.Generations.Generation)
                        {
                            foreach (var modModelGen in modelGen.Modifications.Modification)
                            {
                                var modelRdy =  string.IsNullOrWhiteSpace(modModelGen.Model)? string.Empty:modModelGen.Model.Replace(',', '.').ToString();
                                var generationRdy =  string.IsNullOrWhiteSpace(modModelGen.Generation)? string.Empty:modModelGen.Generation.Replace(',', '.').ToString();
                                var engineRdy = string.IsNullOrWhiteSpace(modModelGen.Engine)? string.Empty:modModelGen.Engine.Replace(',', '.').ToString();
                                var newLine = string.Format("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9}",
                                brandName,
                                modelRdy,
                                generationRdy,
                                engineRdy,
                                (string.IsNullOrWhiteSpace(modModelGen.Yearstart)? string.Empty:modModelGen.Yearstart),
                                (string.IsNullOrWhiteSpace(modModelGen.Yearstop)? string.Empty:modModelGen.Yearstop),
                                (string.IsNullOrWhiteSpace(modModelGen.FuelConsumptionUrban)? string.Empty:modModelGen.FuelConsumptionUrban),
                                (string.IsNullOrWhiteSpace(modModelGen.FuelConsumptionUrbanMin)? string.Empty:modModelGen.FuelConsumptionUrbanMin),
                                (string.IsNullOrWhiteSpace(modModelGen.FuelConsumptionCombined)? string.Empty:modModelGen.FuelConsumptionCombined),
                                (string.IsNullOrWhiteSpace(modModelGen.FuelConsumptionCombinedMin)? string.Empty:modModelGen.FuelConsumptionCombinedMin)
                                ); 
                                strBld.AppendLine(newLine);
                            }
                        }
                    }
                }
                
            }
            System.IO.StreamWriter file = new System.IO.StreamWriter("car_efficiency.txt",true);
            file.WriteLine(strBld.ToString());
            Console.WriteLine("Finished parsing XML");
        }
    }
}
