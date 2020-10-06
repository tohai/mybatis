package com.osstool.mybatis.DAO;

import java.util.List;

import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;

import com.osstool.mybatis.model.Company;

@Mapper
public interface CompanyService {
	
	@Select("select * from company order by id")
	List<Company> selectCompanys();

	@Select("delete from company where id=#{id}")
	void deleteCompanys(int id);
	
	@Select("select * from company where id=#{id}")
	List<Company> selectCompany(int id);
	
	@Update("UPDATE company SET name = #{name}, website = #{website} WHERE id = #{id}")
	void updateCompany(Company Company);

	@Insert("insert into (name,website) values (#{name},#{website})")
	void addCompany(Company Company);

}
