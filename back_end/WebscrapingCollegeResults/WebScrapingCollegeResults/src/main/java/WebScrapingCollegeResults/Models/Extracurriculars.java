package WebScrapingCollegeResults.Models;

import jakarta.persistence.*;

import java.lang.reflect.Array;
import java.util.ArrayList;

@Entity
@Table(name = "ecs")
public class Extracurriculars {

    @Id
    @Column(name = "id")
    private int ID;

    @Column(name = "listofecs")
    private ArrayList<String> ecsList;

    @ManyToOne
    @JoinColumn(name = "\"Attributeid\"", referencedColumnName = "timestamp") // Adjusted to reference the foreign key column
    private Attributes attributeID;



}
