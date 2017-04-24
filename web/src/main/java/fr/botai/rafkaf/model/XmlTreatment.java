package fr.botai.rafkaf.model;

import java.time.LocalTime;
import java.util.ArrayList;
import java.util.List;

import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathExpression;
import javax.xml.xpath.XPathExpressionException;
import javax.xml.xpath.XPathFactory;

import org.w3c.dom.Document;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

public class XmlTreatment {

	public static Document stripEmptyNode(Document document) throws XPathExpressionException{
		XPathFactory xpathFactory = XPathFactory.newInstance();
		// XPath to find empty text nodes.
		XPathExpression xpathExp = xpathFactory.newXPath().compile(
		    "//text()[normalize-space(.) = '']");  
		NodeList emptyTextNodes = (NodeList) 
		    xpathExp.evaluate(document, XPathConstants.NODESET);
		// Remove each empty text node from document.
		for (int i = 0; i < emptyTextNodes.getLength(); i++) {
		  Node emptyTextNode = emptyTextNodes.item(i);
		emptyTextNode.getParentNode().removeChild(emptyTextNode);
		}
		
		return document;
	}
	
	public static List<Rate> parseRatesXML(NodeList nodeList){
		List<Rate> rates = new ArrayList<>();
		for(int i = 0; i < nodeList.getLength(); i++){
			Rate temp = new Rate();
			temp.setSymbol(nodeList.item(i).getAttributes().getNamedItem("Symbol").getTextContent());
			temp.setBid(Float.parseFloat(nodeList.item(i).getChildNodes().item(0).getTextContent()));
			temp.setAsk(Float.parseFloat(nodeList.item(i).getChildNodes().item(1).getTextContent()));
			String[] time = nodeList.item(i).getChildNodes().item(5).getTextContent().split(":");
			temp.setLast(LocalTime.of(Integer.parseInt(time[0]),Integer.parseInt(time[1]),Integer.parseInt(time[2])));
			rates.add(temp);
		}
		
		return rates;
	}
	
}
