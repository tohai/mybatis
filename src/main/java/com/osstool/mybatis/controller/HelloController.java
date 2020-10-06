package com.osstool.mybatis.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.osstool.mybatis.DAO.CompanyService;
import com.osstool.mybatis.model.Company;

@RestController
public class HelloController {
	
	@Autowired
	CompanyService comservice;
	/**
	 * home page
	 * @return
	 */
	@GetMapping(value = "/")
	public String home() {
		List<Company> companies = comservice.selectCompanys();
		
		return companies.get(0).getName();
	}

}
