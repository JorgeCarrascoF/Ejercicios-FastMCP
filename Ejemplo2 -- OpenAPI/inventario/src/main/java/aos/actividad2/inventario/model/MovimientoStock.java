package aos.actividad2.inventario.model;

import jakarta.persistence.Entity;
import jakarta.persistence.EnumType;
import jakarta.persistence.Enumerated;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;
import java.time.LocalDateTime;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "movimientos_stock")
public class MovimientoStock {

  @Id
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  private Long id;

  @Enumerated(EnumType.STRING)
  private TipoMovimiento tipo;

  private Integer cantidad;
  private LocalDateTime fechaMovimiento;

  @Enumerated(EnumType.STRING)
  private OrigenMovimiento origen;

  private Long origenId;

  @ManyToOne
  @JoinColumn(name = "producto_id")
  private Producto producto;
}
