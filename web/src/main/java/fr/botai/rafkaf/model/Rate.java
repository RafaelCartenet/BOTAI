package fr.botai.rafkaf.model;

import java.time.LocalTime;

public class Rate {

	private float bid;
	private float ask;
	private LocalTime last;
	private String symbol;
	
	public Rate(float bid, float ask, LocalTime last, String symbol) {
		super();
		this.bid = bid;
		this.ask = ask;
		this.last = last;
		this.symbol = symbol;
	}

	public Rate() {
		// TODO Auto-generated constructor stub
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

	public String getSymbol() {
		return symbol;
	}

	public void setSymbol(String symbol) {
		this.symbol = symbol;
	}

	@Override
	public String toString() {
		return "Rate [bid=" + bid + ", ask=" + ask + ", last=" + last + ", symbol=" + symbol + "]";
	}
	
	
}
