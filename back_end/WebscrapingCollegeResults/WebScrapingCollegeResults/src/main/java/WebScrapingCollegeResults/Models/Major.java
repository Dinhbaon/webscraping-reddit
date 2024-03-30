package WebScrapingCollegeResults.Models;

import jakarta.persistence.*;

import java.lang.reflect.Array;
import java.util.ArrayList;

@Entity
@Table(name = "major")
public class Major {

    @Id
    @Column(name = "id")
    private int ID;

    @Column(name = "majorlist")
    private ArrayList<String> majorList;

    @ManyToOne
    @JoinColumn(name = "\"Attributeid\"", referencedColumnName = "timestamp") // Adjusted to reference the foreign key column
    private Attributes attributeID;



}
