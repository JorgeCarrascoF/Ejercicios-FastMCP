package aos.actividad2.inventario.model;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.OneToMany;
import jakarta.persistence.Table;
import java.time.LocalDateTime;
import java.util.List;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "productos")
public class Producto {

  @Id
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  private Long id;

  private String nombre;
  private String descripcion;
  private String categoria;
  private Double precio;
  private Integer stock;
  private Integer umbralStock;
  private LocalDateTime fechaCreacion;
  private LocalDateTime fechaUltimaActualizacion;

  @OneToMany(mappedBy = "producto")
  private List<MovimientoStock> movimientoStocks;
}
