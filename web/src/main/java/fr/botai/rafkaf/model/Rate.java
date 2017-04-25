package fr.botai.rafkaf.model;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;
import javax.validation.constraints.NotNull;

@Entity
@Table(name="rates")
public class Rate {

	@Id @GeneratedValue(strategy=GenerationType.AUTO)
	private int id;
	
	@NotNull
	private float bid;
	
	@NotNull
	private float ask;
	
	@NotNull
	@Column(name="date_rate")
	private LocalDateTime last;
	
	@NotNull
	private String symbol;
	
	public Rate(int id, float bid, float ask, LocalDateTime last, String symbol) {
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

	public LocalDateTime getLast() {
		return last;
	}

	public void setLast(LocalDateTime last) {
		this.last = last;
	}

	public void setLastFromTime(LocalTime time){
		this.last = LocalDateTime.of(LocalDate.now(), time);
	}
	
	public String getSymbol() {
		return symbol;
	}

	public void setSymbol(String symbol) {
		this.symbol = symbol;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	@Override
	public String toString() {
		return "Rate [bid=" + bid + ", ask=" + ask + ", last=" + last + ", symbol=" + symbol + "]";
	}
	
	
}
