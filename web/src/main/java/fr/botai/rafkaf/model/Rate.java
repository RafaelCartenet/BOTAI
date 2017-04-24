package fr.botai.rafkaf.model;

import java.time.LocalTime;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties(ignoreUnknown = true)
public class Rate {

	private float bid;
	private float ask;
	private LocalTime last;
	
	public Rate(float bid, float ask, LocalTime last) {
		super();
		this.bid = bid;
		this.ask = ask;
		this.last = last;
	}

	public float getBid() {
		return bid;
	}

	public void setBid(float bid) {
		this.bid = bid;
	}

	public float getAsk() {
		return ask;
	}

	public void setAsk(float ask) {
		this.ask = ask;
	}

	public LocalTime getLast() {
		return last;
	}

	public void setLast(LocalTime last) {
		this.last = last;
	}
	
	
}
