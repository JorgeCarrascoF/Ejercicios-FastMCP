package aos.actividad2.inventario;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import aos.actividad2.inventario.model.Producto;
import aos.actividad2.inventario.repository.ProductoRepository;

@SpringBootApplication
public class InventarioApplication {

	public static void main(String[] args) {
		SpringApplication.run(InventarioApplication.class, args);
	}

	@Bean
	public CommandLineRunner initProductos(ProductoRepository productoRepository) {
		return args -> {
			if (productoRepository.count() == 0) {
				productoRepository.save(new Producto(
					null,
					"Laptop",
					"Laptop de alto rendimiento",
					"Electrónica",
					1200.0,
					10,
					2,
					java.time.LocalDateTime.now(),
					java.time.LocalDateTime.now(),
					null
				));
				productoRepository.save(new Producto(
					null,
					"Mouse",
					"Mouse óptico inalámbrico",
					"Accesorios",
					25.0,
					50,
					10,
					java.time.LocalDateTime.now(),
					java.time.LocalDateTime.now(),
					null
				));
				productoRepository.save(new Producto(
					null,
					"Teclado",
					"Teclado mecánico retroiluminado",
					"Accesorios",
					60.0,
					30,
					5,
					java.time.LocalDateTime.now(),
					java.time.LocalDateTime.now(),
					null
				));
			}
		};
	}

}
