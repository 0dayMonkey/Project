package com.rider.game;

import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Input;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.OrthographicCamera;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.graphics.glutils.ShapeRenderer;
import com.badlogic.gdx.math.MathUtils;
import com.badlogic.gdx.math.Rectangle;
import com.badlogic.gdx.math.Vector2;
import com.badlogic.gdx.utils.Array;



class Plateforme {
	Rectangle rect;
	float angle;

	public Plateforme(Rectangle rect, float angle) {
		this.rect = rect;
		this.angle = angle;
	}
}

public class rider extends ApplicationAdapter {
	SpriteBatch batch;
	TextureRegion motoRegion;
	OrthographicCamera camera;
	Texture moto;
	Rectangle motoRect;
	Vector2 position, vitesse;
	Array<Plateforme> plateformes;
	float distanceEntrePlateformes;
	ShapeRenderer shapeRenderer;

	@Override
	public void create() {
		batch = new SpriteBatch();
		shapeRenderer = new ShapeRenderer();


		camera = new OrthographicCamera();
		camera.setToOrtho(false, Gdx.graphics.getWidth(), Gdx.graphics.getHeight());

		moto = new Texture("moto.png");
		position = new Vector2(50, 200);
		vitesse = new Vector2(0, 0);
		motoRect = new Rectangle(position.x, position.y, moto.getWidth(), moto.getHeight());
		motoRegion = new TextureRegion(moto);
		plateformes = new Array<>();
		distanceEntrePlateformes = 180;
		float hauteurPrecedente = 200;
		for (int i = 0; i < 5; i++) {
			float angle = MathUtils.random(-30, 30);
			float largeur = 200;
			float hauteur = hauteurPrecedente + (float) Math.tan(Math.toRadians(angle)) * largeur;
			plateformes.add(new Plateforme(new Rectangle(i * distanceEntrePlateformes, hauteurPrecedente, largeur, 20), angle));
			hauteurPrecedente = hauteur;
		}
	}

	@Override
	public void render() {
		Gdx.gl.glClearColor(1, 1, 1, 1);
		Gdx.gl.glClear(GL20.GL_COLOR_BUFFER_BIT);

		camera.position.x = position.x + 50;
		camera.update();

		batch.setProjectionMatrix(camera.combined);
		shapeRenderer.setProjectionMatrix(camera.combined);

		batch.begin();
		if (Gdx.input.isKeyPressed(Input.Keys.SPACE)) {
			vitesse.x = 200;
		} else {
			vitesse.x *= 0.98f;
		}

		vitesse.y -= 9.8f;
		position.add(vitesse.x * Gdx.graphics.getDeltaTime(), vitesse.y * Gdx.graphics.getDeltaTime());
		motoRect.setPosition(position.x, position.y);

		float angleMoto = 0;
		boolean onPlatform = false;
		for (Plateforme plateforme : plateformes) {
			if (motoRect.overlaps(plateforme.rect)) {
				onPlatform = true;
				position.y = plateforme.rect.y + plateforme.rect.height;
				vitesse.y = 0;
				motoRect.y = position.y;
				angleMoto = plateforme.angle;
				break;
			}
		}
		if (!onPlatform) {
			angleMoto = 0;
		}


		batch.draw(motoRegion, position.x, position.y, moto.getWidth() / 2, moto.getHeight() / 2, moto.getWidth(), moto.getHeight(), 1, 1, angleMoto);
		batch.end();

		shapeRenderer.begin(ShapeRenderer.ShapeType.Filled);
		for (Plateforme plateforme : plateformes) {
			shapeRenderer.setColor(0.5f, 0, 1, 1);
			shapeRenderer.identity();
			shapeRenderer.translate(plateforme.rect.x, plateforme.rect.y, 0);
			shapeRenderer.rotate(0, 0, 1, plateforme.angle);
			shapeRenderer.rect(0, 0, plateforme.rect.width, plateforme.rect.height);
		}
		shapeRenderer.end();

		genererPlateformes();
		if (position.y < -moto.getHeight()) {
			position.set(50, 200);
			vitesse.set(0, 0);
			motoRect.setPosition(position.x, position.y);
			plateformes.clear();
			float startX = 0;
			for (int i = 0; i < 10; i++) {
				float angle = MathUtils.random(-30, 30);
				float largeur = 200;
				float hauteur = (i == 0) ? 200 : plateformes.peek().rect.y + (float) Math.tan(Math.toRadians(angle)) * largeur;
				plateformes.add(new Plateforme(new Rectangle(startX, hauteur, largeur, 20), angle));
				startX += largeur;
			}
			camera.position.set(camera.viewportWidth / 2, camera.viewportHeight / 2, 0);
		}

	}

	private void genererPlateformes() {
		if (camera.position.x - (camera.viewportWidth / 2) > plateformes.first().rect.x + plateformes.first().rect.width) {
			plateformes.removeIndex(0);
			float angle = MathUtils.random(-30, 30);
			float largeur = 200;
			float hauteur = plateformes.peek().rect.y + (float) Math.tan(Math.toRadians(angle)) * largeur;
			plateformes.add(new Plateforme(new Rectangle(plateformes.peek().rect.x + distanceEntrePlateformes, hauteur, largeur, 20), angle));
		}
	}

	@Override
	public void dispose() {
		batch.dispose();
		shapeRenderer.dispose();
		moto.dispose();
	}
}
